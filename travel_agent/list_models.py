import litellm

# Enable debug logging
litellm._turn_on_debug()

# Try a dummy request to trigger model fetching
try:
    litellm.completion(
        model="openrouter/openai/gpt-3.5-turbo",  # This should be a valid fallback
        messages=[{"role": "user", "content": "Hello!"}],
        api_key="your_openrouter_api_key_here"  # Optional: set via env instead
    )
except Exception as e:
    print("\n🔥 Model fetch attempted. Now check the logs above for available model info.\n")
