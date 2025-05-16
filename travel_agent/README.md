# ✈️ Travel Planner Agent

A smart, Gemini-powered AI assistant that builds personalized travel itineraries based on user goals, preferences, and destination. Perfect for solo travelers, remote workers, or couples planning weekend escapes.

---

## 🌍 What is This Agent?
This agent is built using the Google Agent Development Kit (ADK) and extends the [LiteLLM Agent pattern](https://google.github.io/adk-docs/tutorials/agent-team/#step-2-going-multi-model-with-litellm-optional).

It uses:
- `gemini-2.0-flash` for fast response
- The `google_search` tool to enrich recommendations (optionally extendable)
- Markdown-formatted structured itinerary generation

---

## 🛠️ Setup

### 1. Activate your virtual environment
```bash
# From root directory of the repo
source .venv/bin/activate
```

### 2. Set up API credentials
- Rename `.env.example` to `.env` inside the `travel_planner/` folder
- Add your API key:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GOOGLE_API_KEY=your-api-key-here
```

---

## 🚀 How to Run the Agent

From the root directory of the repo:

```bash
adk web
```

- Navigate to [http://localhost:8000](http://localhost:8000)
- Select `travel_planner` from the dropdown
- Start prompting the agent in the UI

---

## 💬 Example Prompts

- "Plan a 3-day foodie trip to Tokyo focused on local culture"
- "Weekend getaway in Lisbon with historic sites and beach time"
- "I have $1,000 and want to visit Latin America for 5 days"

---

## ✅ Expected Output Format

```markdown
## Day 1 – Arrival and Street Food
- Land at Haneda Airport, check in at Hotel Gracery Shinjuku
- Explore Golden Gai district
- Dinner at Ichiran Ramen

## Day 2 – Culture and Shopping
- Morning at Meiji Shrine
- Visit Harajuku for street fashion
- TeamLab Planets immersive art museum

## Day 3 – Food Markets + Departure
- Tsukiji Outer Market
- Grab souvenirs from Shibuya
- Return to airport
```

---

## 🧠 Why This Agent Matters
Traditional travel search tools can't synthesize structured, context-aware itineraries tailored to user mood, budget, and goals. This agent shows how AI can:

- Adapt travel suggestions in real time
- Personalize without fixed workflows
- Build useful output for end-users (Markdown, JSON, etc.)

---

## ⚠️ Limitations
- Currently uses only one built-in tool (`google_search`)
- Does not yet support flight/hotel APIs
- No persistent memory (Week 3 feature!)

---

## 📚 Resources
- [ADK Tools Overview](https://google.github.io/adk-docs/tools/built-in-tools/)
- [Gemini Model Reference](https://ai.google.dev/gemini-api/docs/models)
- [LiteLLM Integration](https://docs.litellm.ai/docs/)

---

## 📎 Next Up
- Add ML trip classifier (Week 2)
- Integrate vector-based preference storage (Week 3)
- Build a multi-agent planner + recommender (Week 4+)

---

> Built with ❤️ using ADK and Gemini
