# `cache.set` reference

Stores a value under a key with an optional time-to-live.

## Signature

`cache.set(key, value, ttl=None)`

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `key` | string | yes | — | Cache key. Max 255 characters. |
| `value` | bytes | yes | — | Serialized value. Max 1 MiB. |
| `ttl` | integer | no | `None` | Seconds until expiry. `None` means no expiry. |

## Returns

`True` on success. Raises `CacheError` if the backend is unreachable.

## Example

```python
cache.set("session:42", b"...", ttl=3600)
```
