# Agentic AI Course Notes

## Creating an AI Agent

### Logic Flow: Autonomous Digital Decision Maker
1. **Why**: Purpose and context
2. **What**: Architecture: input
3. **Process**: Process it
4. **Output**: Output
5. **How**: Thinking part
6. **Structure**: How to structure (architecture/design)
7. **Building**: Building → improve → scale it (multi-agent ecosystem)

### Vision/Agenda of the Agent
- Perceive
- Reason/Cognition
- Act
- Learn
- Collaboration
- Security

### Agentic AI Modules
- An Agentic AI system would comprise multiple modules
- Each module would correspond to a component of the agent's agenda/vision
- These modules handle specific functions like perception, reasoning, action, learning, collaboration, and security

### Technical Flow Diagram: Agentic Patterns and Versioning
- Core agentic patterns should follow versioning principles
- Base pattern is V1 (e.g., basic input-process-output flow)
- When new capabilities are introduced (e.g., reflection), increment to V2
- Each version represents an evolution of the core agentic patterns
- These versions help identify and track different agentic capabilities

### Different Design Patterns
- **Layered Architecture**: Divide the brain into distinct levels with clear segregation
  - Perception layer: See/observe the environment
  - Planning layer: Think/plan actions
  - Action layer: Execute/act on decisions
- **Blackboard Architecture**: Shared workspace used by all agents
  - Shared memory or workspace accessible to multiple agents
  - Example: Hospital scenario where doctors write on shared patient charts
  - Facilitates collaboration and information sharing between different modules
- **Subsumption Architecture**: Building brain-like layers with bottom-up approach
  - Start with simple, reflexive actions and behaviors
  - Progress to more complex and advanced actions/tasks
  - Higher layers can subsume/override lower layer behaviors
  - Rarely used in modern agents
- **Hybrid Architecture**: Combines reactive and planning behaviors
  - Mix of fast reflex actions and smart thinking/planning
  - Balances immediate responses with thoughtful decision-making
  - Incorporates both reactive and deliberative components
  - Examples: Drones, delivery agents, autonomous vehicles

**Focus**: We will work primarily with Hybrid Architecture

### Hybrid Architecture Implementation in Code
- **React**: The agent responds to user input (the `input("Enter your prompt: ")` line)
- **Plan**: The processing happens in the `ai_agent` function where the prompt is sent to the model
- **Act**: The agent performs the action by calling `model.generate_content(prompt)`
- **Input**: User-provided prompt via input() function
- **Process**: The AI model processes the prompt
- **Output**: The response is printed to the console

### Agent Evolution

#### Base Agent (Initial Version)
- **Reactive Only**: Simply reacts to input without any proactive behavior
- **No Tool Usage**: Cannot interact with external tools or systems
- **No Verification**: Accepts and processes information without validation
- **Limited Autonomy**: Requires direct user input to function
- **Basic I/O**: Simple input-process-output pattern

#### Advanced Agent (Evolved Version)
- **Proactive Behavior**: Can initiate actions without direct user input
- **Tool Integration**: Can use external tools and APIs
- **Verification Capabilities**: Validates information and cross-checks facts
- **Planning**: Can create and execute multi-step plans
- **Memory**: Retains information across conversations
- **Self-correction**: Can identify and fix its own mistakes

### Reflection Pattern
- **First Step in Evolution**: Moving beyond simple text generation to self-review
- **Review Process**: Agent examines its own output before finalizing
- **Quality Assessment**: Evaluates the accuracy, relevance, and appropriateness of generated content
- **Iterative Improvement**: Makes adjustments based on self-evaluation
- **Meta-cognition**: Thinking about its own thinking process
- **Self-validation**: Checks its responses against known facts or constraints
- **Not just output**: The agent considers the implications and quality of its output

#### Reflection Process Steps:
1. **Evaluate**: Assess the initial output for quality, accuracy, and completeness
   - Score the response against the original prompt
   - Check for factual accuracy
   - Verify completeness of the answer
   - Assess tone and appropriateness

2. **Reflect**: Consider what aspects might need improvement or refinement
   - Identify gaps in information
   - Recognize potential biases or errors
   - Consider alternative approaches
   - Analyze scope of possible improvements

3. **Refine**: Make adjustments to improve the response based on self-assessment
   - Correct any identified errors
   - Add missing information
   - Improve clarity and structure
   - Enhance the overall quality of the response

#### Scope of Improvements in Reflection:
- **Accuracy**: Fact-checking and correcting information
- **Relevance**: Ensuring the response addresses the prompt
- **Completeness**: Filling in missing information
- **Clarity**: Improving readability and understanding
- **Consistency**: Maintaining logical flow and coherence
- **Tone**: Adjusting for appropriate context and audience
- **Structure**: Organizing information better
- **Creativity**: Enhancing originality where needed

### Tool Use Pattern
- **Next Evolution Step**: Agents begin to interact with external tools and APIs
- **External Information**: Agents can access real-time data from external sources
- **Example**: For "What's the temperature in London?", the agent retrieves current weather data from an external API
- **Enhanced Capabilities**: No longer limited to pre-trained knowledge; can access current, dynamic information
- **Integration**: Combines external data with AI processing to provide more accurate, up-to-date responses
- **Autonomy Level**: Agent must determine when and which tools to use based on the query
- **Verification**: Cross-checks external information with other sources when possible

#### Tool Use Capabilities:
- **API Integration**: Connect to various web services and databases
- **Data Retrieval**: Fetch real-time information (weather, news, stock prices, etc.)
- **Action Execution**: Perform external tasks (send emails, book appointments, etc.)
- **Multi-step Operations**: Chain multiple tools together for complex tasks
- **Adaptive Tool Selection**: Choose appropriate tools based on context and requirements

### REACT Pattern
- **Reasoning + Acting**: Combines reasoning with action in a cyclical process
- **Goal-Oriented**: Continues until the specified goal is achieved
- **Iterative Process**: Repeatedly observes, reasons, plans, acts, and re-evaluates
- **Continuous Loop**: Reason → Act → Observe → Reason → Act → ... until goal completion
- **Adaptive Behavior**: Adjusts approach based on outcomes of previous actions
- **Feedback Integration**: Uses results of actions to inform future decisions
- **Distinct from Reflection**: While reflection evaluates a completed response, REACT influences how the response is created through iterative reasoning and action
- **Implementation Strategy**: Can delegate specific tasks or planning to specialized agents (e.g., delegating plan execution to base_agent)

#### REACT Cycle:
1. **Reason**: Analyze the current situation and determine what needs to be done
2. **Act**: Execute an action based on the reasoning
3. **Observe**: Monitor the outcome of the action
4. **Re-think**: Evaluate the result and adjust the plan if needed
5. **Repeat**: Continue the cycle until the goal is achieved

### Additional Evolution Patterns for Your Agent

#### Memory Integration
- **Short-term Memory**: Retain conversation context within a session
- **Long-term Memory**: Store and recall information across multiple sessions
- **Knowledge Accumulation**: Learn from past interactions to improve future responses

#### Multi-Agent Collaboration
- **Agent Teams**: Multiple specialized agents working together
- **Task Distribution**: Dividing complex tasks among different agents
- **Communication Protocols**: Agents sharing information and coordinating actions

### Reflective Agent Implementation
- **Critic Role**: Evaluates responses generated by the base agent
- **Quality Assessment**: Checks for accuracy, relevance, completeness, and clarity
- **Feedback Loop**: Provides feedback that can be used to improve responses
- **Separate Module**: Implemented as a distinct component that can be integrated with the base agent

### Prompt Evolution
- **Simple Prompts**: Basic instructions like "Review this response"
- **Structured Prompts**: More detailed instructions with specific evaluation criteria
- **Multi-step Prompts**: Breaking down the reflection process into distinct steps (evaluate, reflect, refine)
- **Meta-prompting**: Prompts that teach the agent how to evaluate its own responses
- **Your Current Prompt**: "Review the following response for improvements..." is a good start but could be more structured

#### Planning & Forecasting
- **Multi-step Planning**: Breaking complex goals into manageable steps
- **Scenario Modeling**: Predicting outcomes of different approaches
- **Resource Management**: Optimizing use of computational and external resources

#### Self-Modification & Learning
- **Adaptive Parameters**: Adjusting behavior based on feedback
- **Skill Acquisition**: Learning new capabilities over time
- **Performance Optimization**: Improving efficiency based on usage patterns

#### Ethical Reasoning
- **Bias Detection**: Identifying and correcting biased responses
- **Ethical Filters**: Applying moral and ethical guidelines to responses
- **Transparency**: Explaining reasoning behind decisions

### What Makes Prompts Better? (Mentor Discussion)
- **Explicit Role Assignment**: Defining a specific role like "You are an expert literature critic" or "You are a technical reviewer"
- **Clear Evaluation Criteria**: Specifying what to look for (accuracy, relevance, completeness, clarity, tone)
- **Structured Format**: Providing a format for the response (e.g., bullet points, sections)
- **Context**: Including the original prompt to maintain context during evaluation
- **Specific Instructions**: Instead of "improve it," specify "check for factual accuracy" or "enhance clarity"

### Better Prompt Structure for Your Reflective Agent:
```
You are an expert AI response evaluator. Your task is to critically assess the quality of responses.

Original Prompt: {original_prompt}
Response to Evaluate: {response}

Evaluate this response based on these criteria:
1. Accuracy: Are the facts correct?
2. Relevance: Does it address the original query?
3. Completeness: Are important aspects covered?
4. Clarity: Is it easy to understand?

Provide specific feedback for each criterion and then a refined version addressing these points.
```

### What Helps Better in Evaluations? (Mentor Discussion)

#### Scoring Systems
- **Numerical Scale**: 1-5 or 1-10 scales provide quantifiable metrics
- **Descriptive Scale**: Poor/Average/Good/Excellent provides qualitative assessment
- **Weighted Scoring**: Different criteria have different importance based on context
- **Justification Required**: Scores must include reasoning (not just numbers)

#### Effective Evaluation Components
- **Clear Criteria Definitions**: Each evaluation criterion should be well-defined
- **Context Preservation**: Maintaining original prompt context during evaluation
- **Reasoning Transparency**: Explaining why specific scores were given
- **Actionable Feedback**: Feedback should guide the refinement process
- **Balanced Assessment**: Both positive and negative aspects should be noted
- **Specificity**: Feedback should be specific rather than generic

#### Multi-step Evaluation Process
1. **Assessment**: Score each criterion with detailed reasoning
2. **Prioritization**: Identify which issues are most important to address
3. **Recommendation**: Provide specific suggestions for improvements
4. **Refinement**: Generate an improved version based on feedback

### Reflection vs REACT - When to Use Each (Mentor Discussion)

#### Reflection Pattern
- **Purpose**: Evaluates a completed response/output
- **Process**: Takes a finished answer and critiques it
- **Focus**: Quality assessment of what has already been produced
- **Timing**: Post-production evaluation
- **Example**: Reviewing a draft essay after it's written

#### REACT Pattern
- **Purpose**: Guides the creation of responses through iterative reasoning
- **Process**: Interleaves thinking and acting during production
- **Focus**: How the response should be created, step by step
- **Timing**: During-production decision making
- **Example**: Writing an essay while continuously checking and adjusting direction

#### Choosing Between Them
- Use **Reflection** when you want to improve an existing output
- Use **REACT** when you want to build better outputs from the start
- **REACT** is more proactive (guides creation)
- **Reflection** is more reactive (improves after creation)