# Edureka Agentic AI Course

This repository contains the code, notes, and experiments from the Edureka Agentic AI course. It documents the journey from basic reactive agents to sophisticated planning and reasoning agents.

## Course Overview

The Edureka Agentic AI course covers the fundamental concepts, implementations, and best practices for building autonomous AI agents. This repository chronicles the evolution from simple reactive agents to complex, reasoning-based systems.

## Learning Modules

### 1. Core Components of Agentic AI
- **Plans**: The agent's ability to create, maintain, and execute multi-step plans to achieve goals
- **Memory**: The agent's ability to store, retrieve, and utilize information over different time scales
- **Tools**: The agent's ability to interface with external systems, APIs, and resources

### 2. Agent Evolution Patterns
- **Base Agent (V1)**: Simple reactive agent with basic input-process-output flow
- **Reflective Agent (V2)**: Enhanced agent with self-evaluation and refinement capabilities
- **REACT Agent (V3)**: Advanced agent with planning, reasoning, and reflection phases
- **Workflow vs Planning Agents**: Understanding orchestration-heavy vs dynamic decision-making agents

### 3. Technical Concepts Covered
- **Tokens and Token Length**: Understanding how AI models process text in token chunks
- **Context Windows**: Managing the maximum number of tokens a model can process at once
- **Temperature, Top-p, Top-k**: Controlling response creativity and randomness
- **Embedding Models**: Token-to-vector mapping for semantic understanding
- **Hallucination Prevention**: Strategies for ensuring factual accuracy
- **RAG Systems**: Retrieval-Augmented Generation for knowledge grounding

### 4. Agent Types and Architecture
- **Workflow Agents**: Orchestration-heavy agents using decision trees for predetermined workflows
- **Planning Agents**: Dynamic agents where the LLM decides next steps based on observations
- **LLM + Tools + Memory**: Core architecture of modern agentic systems

## Project Structure

```
├── base_agent.py              # Simple reactive agent (V1)
├── reflective_agent.py        # Self-evaluating agent (V2) 
├── react_agent.py             # Multi-phase planning agent (V3)
├── config/
│   └── settings.py            # Configuration and API key management
├── agentic_ai_course_notes.md # Comprehensive course notes and concepts
├── base_agent_analysis.md     # Analysis of base agent implementation
├── reflective_agent_analysis.md # Analysis of reflective agent implementation
├── react_agent_analysis.md    # Analysis of REACT agent implementation
├── mentor_synthesis_guide.md  # Mentor's comprehensive guidance
├── python_migration_notes.md  # Python version migration documentation
├── QWEN.md                   # Learning framework and guidelines
└── experiment_log.md         # Results from November 9, 2025 multi-agent experiment
```

## Key Experiments and Results

### November 9, 2025 Multi-Agent System Analysis
- **Prompt**: "what is genai"
- **Results**:
  - Base Agent: Provided comprehensive foundational knowledge with solid structure
  - Reflective Agent: Significantly enhanced quality through draft-refinement cycle
  - REACT Agent: Produced most comprehensive, professionally structured output

**Key Finding**: Progressive enhancement where each agent layer added value to the response, demonstrating the effectiveness of multi-phase processing.

## Technical Setup

### Requirements
- Python 3.12 (as of November 16, 2025)
- Google Generative AI SDK (`google-generativeai`)
- Python-dotenv for environment management
- uv for package management

### Python Migration
The project now uses Python 3.12 to align with course requirements. See `python_migration_notes.md` for detailed migration process.

## Implementation Highlights

### Base Agent (V1)
- Simple reactive behavior
- Direct interaction with Google's Gemini API
- Foundation for enhancement strategies

### Reflective Agent (V2)
- Two-phase process: Draft → Review → Refinement
- Implements self-evaluation concept
- Shows understanding of iterative improvement

### REACT Agent (V3)
- Three-phase approach: Plan → Reason → Reflect
- Multi-stage quality assurance process
- Produces most comprehensive outputs

### Practical Examples
- **Customer Support Agent**: Workflow agent with decision trees
- **Stock Research Agent**: Planning agent with dynamic adaptation
- **Code Generation/Debugging Agent**: Planning agent with iterative problem-solving

## Evaluation and Benchmarking

The course covers various approaches to LLM evaluation:
- **Static Evaluation**: Using predefined datasets with known answers
- **Live Evaluation**: Real-time human evaluation of outputs
- **Ground Truth vs Human Preference**: Different metrics for accuracy vs satisfaction

## Hallucination Prevention Strategies

Three-tier approach to addressing hallucinations:
1. **Prompting Fixes**: Grounding, citations, uncertainty expression
2. **Retrieval Fixes**: RAG with reranking, query expansion, vector indexing
3. **Fine-tuning Fixes**: Specialized training on domain-specific data

## Learning Framework

This repository follows the structured learning framework documented in `QWEN.md`:
- Raw notes capture and enhancement
- Mentor perspective integration
- Implementation connection to concepts
- Continuous evaluation and improvement

## Future Development Path

Based on the mentor's recommendations:
1. Add RAG capabilities for external knowledge access
2. Implement comprehensive memory systems (short and long-term)
3. Develop tool usage capabilities
4. Consider domain-specific fine-tuning after establishing patterns
5. Enhance dynamic planning aspects

## Key Insights

1. **Progressive Complexity**: Each agent version builds upon previous foundations
2. **Quality Through Process**: Multi-phase agents produce significantly better outputs
3. **Context Management**: Token limits and position effects are critical considerations
4. **Hallucination Mitigation**: Multiple strategies needed for reliable outputs
5. **Agent Type Selection**: Choose workflow vs planning agents based on task predictability

## Next Steps

- Implement RAG systems with external knowledge bases
- Add tool usage capabilities to agents
- Develop long-term memory solutions
- Explore domain-specific fine-tuning
- Continue evaluation and refinement of existing implementations

## Resources

- `agentic_ai_course_notes.md`: Complete course notes with concepts and mentor insights
- `mentor_synthesis_guide.md`: Comprehensive analysis and strategic guidance
- `experiment_log.md`: Detailed results from multi-agent experiments
- Analysis files: Deep technical analysis of each implementation

---

*This repository is actively maintained as part of the Edureka Agentic AI learning journey.*