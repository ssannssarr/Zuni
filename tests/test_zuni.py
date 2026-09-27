import json

import pytest

from zuni.llm import config as config_module
from zuni.llm.llm import LLM


def test_save_and_load_config(tmp_path, monkeypatch):
    config_dir = tmp_path / ".config" / "zuni"
    config_file = config_dir / "config.json"

    monkeypatch.setattr(config_module, "CONFIG_DIR", config_dir)
    monkeypatch.setattr(config_module, "CONFIG_FILE", config_file)

    config_module.save_config(
        api_key="test-key",
        model="test-model",
        base_url="https://example.com/v1",
    )

    assert config_module.load_config() == {
        "API_KEY": "test-key",
        "MODEL": "test-model",
        "BASE_URL": "https://example.com/v1/",
    }


def test_load_config_when_file_does_not_exist(tmp_path, monkeypatch):
    config_file = tmp_path / "config.json"
    monkeypatch.setattr(config_module, "CONFIG_FILE", config_file)

    with pytest.raises(RuntimeError, match="Configuration File"):
        config_module.load_config()


def test_api_key_from_environment(monkeypatch):
    monkeypatch.setattr(config_module, "load_config", lambda: {})
    monkeypatch.setenv("OPENROUTER_API_KEY", "env-key")

    assert config_module.api_key() == "env-key"


def test_api_key_from_config(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setattr(
        config_module,
        "load_config",
        lambda: {"API_KEY": "config-key"},
    )

    assert config_module.api_key() == "config-key"


def test_api_key_missing(monkeypatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    monkeypatch.setattr(config_module, "load_config", lambda: {})

    with pytest.raises(RuntimeError, match="API_KEY is not present"):
        config_module.api_key()


def test_model_from_config(monkeypatch):
    monkeypatch.setattr(
        config_module,
        "load_config",
        lambda: {"MODEL": "test-model"},
    )

    assert config_module.model() == "test-model"


def test_model_default(monkeypatch):
    monkeypatch.setattr(config_module, "load_config", lambda: {})

    assert config_module.model() == "openrouter/free"


def test_base_url_from_environment(monkeypatch):
    monkeypatch.setenv("ZUNI_BASE_URL", "https://env.example/v1")
    monkeypatch.setattr(config_module, "load_config", lambda: {})

    assert config_module.baseUrl() == "https://env.example/v1"


def test_base_url_from_config(monkeypatch):
    monkeypatch.delenv("ZUNI_BASE_URL", raising=False)
    monkeypatch.setattr(
        config_module,
        "load_config",
        lambda: {"BASE_URL": "https://config.example/v1"},
    )

    assert config_module.baseUrl() == "https://config.example/v1"


def test_config_combines_values(monkeypatch):
    monkeypatch.setattr(config_module, "api_key", lambda: "key")
    monkeypatch.setattr(config_module, "model", lambda: "model")
    monkeypatch.setattr(config_module, "baseUrl",
                        lambda: "https://example.com/v1")

    assert config_module.Config() == {
        "API_KEY": "key",
        "MODEL": "model",
        "BASE_URL": "https://example.com/v1",
    }


def test_llm_initialization():
    llm = LLM(
        api_key="test-key",
        model="test-model",
        base_url="https://example.com/v1",
    )

    assert llm.api_key == "test-key"
    assert llm.model == "test-model"
    assert str(llm.aclient.base_url) == "https://example.com/v1"


def test_llm_headers():
    llm = LLM(api_key="test-key", model="test-model")

    assert llm.headers() == {
        "Authorization": "Bearer test-key",
        "Content-Type": "application/json",
    }


def test_llm_headers_without_api_key():
    llm = LLM(api_key="", model="test-model")

    with pytest.raises(RuntimeError, match="No api_key found"):
        llm.headers()


def test_llm_payload_without_tools():
    llm = LLM(api_key="test-key", model="test-model")
    chat = [{"role": "user", "content": "Hello"}]

    assert llm.payload(chat=chat) == {
        "model": "test-model",
        "messages": chat,
    }


def test_llm_payload_with_tools():
    llm = LLM(api_key="test-key", model="test-model")
    chat = [{"role": "user", "content": "Hello"}]
    tools = [{"type": "function", "function": {"name": "search"}}]

    assert llm.payload(chat=chat, tools=tools) == {
        "model": "test-model",
        "messages": chat,
        "tools": tools,
    }


@pytest.mark.asyncio
async def test_llm_ask(monkeypatch):
    llm = LLM(
        api_key="test-key",
        model="test-model",
        base_url="https://example.com/v1",
    )

    class FakeResponse:
        def raise_for_status(self):
            pass

        def json(self):
            return {
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": "Hello!",
                        }
                    }
                ]
            }

    async def fake_post(*, url, headers, json):
        assert url == "/chat/completions"
        assert headers["Authorization"] == "Bearer test-key"
        assert json == {
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hello"}],
        }
        return FakeResponse()

    monkeypatch.setattr(llm.aclient, "post", fake_post)

    result = await llm.ask(
        chat=[{"role": "user", "content": "Hello"}],
    )

    assert result["choices"][0]["message"]["content"] == "Hello!"
