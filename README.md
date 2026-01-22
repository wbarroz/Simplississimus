# Simplississimus
Proof of Concept for an Extremely Simple ChatBot

## TL;DR

  1. `git clone https://github.com/wbarroz/Simplississimus`
  1. `cd Simplississimus`
  1. `python -m venv .venv`
  1. `source .venv/bin/activate`
  1. `pip install -r requirements.txt`
  1. `ollama pull qwen3:0.6b`
  1. `python chat.py`

## A little longer description
A very simple ChatBot, pretty limited BUT able to recognize the need to access an external tool(a basic calculator at this time).

  * To allow run locally, devoid of GPU, a ridiculously reduced model was used(ollama qwen3 w/ 0.6b params)
  * The decision is black or white: to rely purely on the knowledge base(VERY limited) or doing the calculation;
  * To simplify the calculator part, the model is forced to input the calculation "python coded", and then it's `eval`ueted.

## TODO
  1. Use a beefier model;
  1. A more nuanced decision(e.g. to allow the model to deal with "mixed" cases);
  1. Include a range of POSSIBLE tools(maybe accepting user API options);


---
