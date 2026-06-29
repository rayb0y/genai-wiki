---
title: "System Architecture Diagram"
type: reference
created: 2026-06-14
updated: 2026-06-14
tags: [architecture, multi-agent, diagram, socratic, orchestrator]
sources: []
---

# System Architecture Diagram

A flow view of the design in [[innovation-team-agent-architecture]]. The team is the only human in the loop. Two agents are team-facing: the Socratic Agent addresses the whole team with one shared question, and each member has their own Collaboration Agent for a private, one-to-one channel (post-session notes, concerns, complaints). The Orchestrator coordinates but never speaks. Each tier box states who may read and write it.

```mermaid
flowchart TB
  TEAM(["Innovation team"])

  subgraph STATE["Shared state, the LLM-Wiki"]
    direction TB
    T1["Tier 1, Project State<br/>decision log, artifact log, current phase<br/>read + write: all agents"]
    T2["Tier 2, Team Dynamics<br/>participation, unresolved positions<br/>write: Collaboration; read: Collaboration + Orchestrator"]
    T3["Tier 3, Knowledge Base<br/>iNPD phase definitions, TRIZ matrix<br/>read-only: all agents"]
    T4["Tier 4, Agent Logs<br/>per-agent logs, Socratic question history<br/>write: each agent; read: Orchestrator"]
  end

  ORCH{{"Orchestrator<br/>reads all four tiers, writes nothing<br/>never speaks to the team<br/>decides if, when, and which question fires"}}

  subgraph MON["Monitoring agents"]
    direction TB
    INPD["iNPD Agent<br/>phase monitor + gate check"]
    COLLAB["Collaboration Agent<br/>one per member, runs between sessions"]
    POW["Proof of Work Agent<br/>logs every artifact"]
  end

  DLOG["Decision Logger<br/>records the why"]
  SOC["Socratic Agent<br/>asks one question, four modes<br/>the only agent that speaks to the team"]

  subgraph MILE["Milestone agents"]
    direction TB
    SYN["Synthesis Agent<br/>at phase transitions"]
    RETRO["Retrospective Agent<br/>at project completion"]
  end

  TEAM -- "artifacts" --> POW
  TEAM -- "session transcripts" --> INPD
  TEAM -- "transcripts + feedback" --> DLOG

  TEAM == "notes, concerns (private, per member)" ==> COLLAB
  COLLAB == "private one-to-one check-ins" ==> TEAM

  INPD -- "phase / gate flags" --> ORCH
  COLLAB -- "participation flags" --> ORCH
  POW -- "missing-rationale events" --> ORCH

  ORCH == "trigger + mode" ==> SOC
  SOC == "one question" ==> TEAM
  TEAM -- "answer, thumbs, documented ignore" --> DLOG

  INPD -- write --> T1
  POW -- write --> T1
  DLOG -- write --> T1
  COLLAB -- write --> T2

  T1 -. read .-> SYN
  T1 -. read .-> RETRO
  SYN -- "synthesis doc" --> TEAM
  RETRO -- "retrospective" --> TEAM

  STATE -. "reads all tiers" .-> ORCH
```

## How to read it

Solid arrows are writes and message passing. Dotted arrows are reads. The thick arrows are the single live intervention path: the Orchestrator triggers the Socratic Agent with a mode, the Socratic Agent asks the team one question, and the team's answer flows to the Decision Logger as the record of why.

Reads not drawn, to keep the graph legible, are stated in each tier box and in the [[innovation-team-agent-architecture]] tier table: the iNPD and Socratic agents read Tier 3 (phase definitions, TRIZ matrix), the Collaboration agents read Tier 1, the Decision Logger reads Tier 4 (the Socratic question history), and the Orchestrator reads all four tiers.

The two rules the diagram is built to enforce: the LLM never decides, so every output is a question or a read, and the team is addressed in only two ways, the Socratic Agent's single question to the whole group and each member's private Collaboration Agent. What a member tells their Collaboration Agent stays private; if it warrants a team-level response, that goes out as a neutral, de-identified Socratic question, never as "someone complained."
