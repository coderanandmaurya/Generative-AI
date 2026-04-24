# Import classes from the langchain_huggingface package
# HuggingFacePipeline -> wraps a local Hugging Face model into a LangChain-compatible LLM
# ChatHuggingFace -> (not used here) is for chat-style / API-based usage, often needs HF token
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


# Create an LLM (Large Language Model) instance using a Hugging Face model
# .from_model_id() loads the model + tokenizer and builds a transformers pipeline internally
llm = HuggingFacePipeline.from_model_id(
    
    # Hugging Face model identifier (downloaded from HF Hub and cached locally)
    # :contentReference[oaicite:0]{index=0}
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    
    # Task type tells transformers which pipeline to use
    # "text-generation" → causal language model (generate continuation of text)
    task="text-generation",
    
    # device=0 means use GPU (CUDA device index 0)
    # -1 would mean CPU
    device=0,
    
    # These parameters control how text is generated (inference-time behavior)
    pipeline_kwargs={
        
        # Controls randomness of output
        # lower (~0.2) = deterministic, higher (~1.0) = more creative
        "temperature": 0.7,
        
        # Maximum number of new tokens the model can generate
        # (not total length, only generated continuation)
        "max_new_tokens": 100,
        
        # Enables sampling-based decoding
        # Required for temperature to have any effect
        # If False → greedy decoding (always picks highest probability token)
        "do_sample": True,
    },
)


# Run inference using the model
# .invoke() is LangChain's standard method to send input to an LLM
# Input: plain string prompt
# Output: plain string (because this is NOT a chat model wrapper)
response = llm.invoke("Hello, how are you?")


# Print the generated response
# Note: response is a string, NOT an object with `.content`
print(response)
