<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pygame-2.5+-green?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Architecture-Object--Oriented-purple?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Game%20Engine-Event--Driven-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>
</p>

<h1 align="center">Snake Arcade Python</h1>

<p align="center">
Polished Arcade Game Implementation • Pygame Engine • Object-Oriented Architecture • Particle Visuals & Power-Ups
</p>

<p align="center">
Arcade Game Loop • Spatial Collision Detection • Dynamic Level Scaling • Local Score Serialization
</p>

---

## Overview

**Snake Arcade Python** is a polished, modern Python and Pygame implementation of the classic Snake arcade game engineered with a clean, modular object-oriented architecture.

Rather than relying on simple script-based game loops, this project structures game mechanics into decoupled entities and specialized modules:

- **Snake Engine:** Controls continuous vector direction, smooth movement interpolation, tail segment management, and directional eye rendering.
- **Food & Power-Up System:** Handles dynamic item spawning, value multi-tier scoring, and active power-up timer logic.
- **Game & Level Controller:** Manages state transitions, collision detection, dynamic obstacle placement, level progression scaling, and event loops.
- **Particle & FX Renderer:** Generates real-time particle visual effects for food ingestion, power-up activation, and dynamic HUD overlays.
- **Score Serialization Manager:** Handles local file I/O operations for reading, updating, and persisting high-score milestones.

The repository demonstrates applied **Software Engineering**, **Object-Oriented Design (OOD)**, **Event-Driven Programming**, and **Game State Management** in Python.

---

## Why This Project Matters

### Elevating Classic Arcade Mechanics

Basic Snake implementations typically have several structural limitations:
- **Monolithic Scripting:** Combining input handling, physics, state update, and rendering inside a single monolithic loop leads to fragile, unmaintainable code.
- **Static Difficulty:** Fixed game speed and lack of environmental hazards result in monotonous gameplay.
- **Lack of Visual Feedback:** Rigid grid blocks and minimal animations diminish player immersion and feedback clarity.

### The Modular Engine Advantage

This project resolves these limitations by applying software engineering best practices:
1. **Decoupled System Responsibilities:** Input processing, physics/collision evaluation, state management, and rendering operate in distinct, testable modules.
2. **Dynamic Difficulty Engine:** As player score increases, level progression dynamically introduces speed scaling and procedural environmental obstacles.
3. **Enhanced Visual Fidelity:** Custom particle emission systems, rounded snake rendering with directional eye orientation, and dynamic HUD components deliver a refined visual experience.

---

## Potential Real-World Applications & Extensibility

- **AI Reinforcement Learning Environment:** Serves as a modular, lightweight baseline environment for training Deep Q-Networks (DQN) or PPO reinforcement learning agents.
- **Pygame Game Architecture Template:** Demonstrates production-grade design patterns for structured 2D game development in Python.
- **Interactive Physics & Particle Prototyping:** Provides reference implementations for custom particle emission systems and spatial grid collision algorithms.
- **Game State Serialization Benchmark:** Illustrates safe, asynchronous local data persistence patterns using standard file I/O operations.

---

## Key Technical Highlights

- **Object-Oriented Architecture:** Decoupled class architecture featuring dedicated `Snake`, `Food`, `Game`, and utility modules.
- **Event-Driven Main Loop:** Clean separation of Pygame event polling, frame rate regulation (`pygame.time.Clock`), state updates, and rendering.
- **Smooth Rounded Visuals & Dynamic Eye Rendering:** Custom vector coordinate drawing rendering smooth snake segments and directional gaze orientation.
- **Procedural Obstacle & Power-Up Engine:** Dynamic spawning logic for high-value food bonuses and level-dependent environmental obstacles.
- **Real-Time Particle FX System:** Emission pipeline generating visual particle bursts upon collision and food consumption.
- **Local Score Persistence:** Automated `highscore.txt` reading and write-back serialization preserving top scores across sessions.
- **Dynamic HUD Overlay:** Real-time rendering of current score, high score, active level, and game state prompts.

---

## Game Architecture & Control Flow

The following diagram illustrates the event loop, state transitions, and component interactions within the game engine.

```text
               User Input (Keyboard Arrows / Space / ESC)
                                   │
                                   ▼
                      ┌────────────────────────┐
                      │  Pygame Event Handler  │
                      │  (Input Handoff & UI)  │
                      └────────────┬───────────┘
                                   │ [Direction Delta / State Switch]
                                   ▼
                      ┌────────────────────────┐
                      │   Snake Game Engine    │
                      │ (Game State Controller)│
                      └────────────┬───────────┘
                                   │
             ┌─────────────────────┴─────────────────────┐
             ▼                                           ▼
┌────────────────────────┐                  ┌────────────────────────┐
│   Snake Movement &     │                  │  Food & Power-Up System│
│  Collision Evaluator   │                  │ (Item & Obstacle Spawn)│
└────────────┬───────────┘                  └────────────┬───────────┘
             │                                           │
             └─────────────────────┬─────────────────────┘
                                   │ [Updated Game State & Positions]
                                   ▼
                      ┌────────────────────────┐
                      │  Visual & HUD Renderer │
                      │ (Particle FX & Canvas) │
                      └────────────┬───────────┘
                                   │ [High Score Trigger]
                                   ▼
                      ┌────────────────────────┐
                      │ Score Persistence I/O  │
                      │     (highscore.txt)    │
                      └────────────┬───────────┘
```

### 1. Game Loop & Input Handoff
The main execution gateway listens for Pygame keyboard events. Directional key inputs are filtered to prevent immediate 180-degree self-collisions before being passed to the `Snake` instance for velocity modification.

### 2. Collision Detection & Spatial Physics
During every tick, the `Game` controller checks coordinate intersections between the snake head, grid boundaries, body segments, food items, and obstacles.

### 3. Rendering Pipeline & Visual Effects
The rendering cycle executes sequentially: background clearing, obstacle drawing, food/power-up rendering, particle updates, snake body segment rendering, and HUD string blitting.

### 4. High-Score Persistence Layer
Upon game over evaluation, if the current score exceeds the cached local record, the updated score is written to `highscore.txt` asynchronously to prevent frame stutter.

---

## Repository Structure

```text
snake-arcade-python/
│
├── snake_game/
│   ├── __init__.py           # Package Initialization
│   ├── main.py               # Package Game Loop Entry Point
│   ├── game.py               # Core Game Engine & State Manager
│   ├── snake.py              # Snake Entity, Movement & Segment Logic
│   ├── food.py               # Food Spawner, Obstacles & Power-Up Engine
│   └── utils.py              # Particle Systems, Colors & HUD Helper Utilities
│
├── main.py                   # Root Execution Gateway
├── highscore.txt             # Local High Score Persistent Storage
├── requirements.txt          # Python Dependencies Manifest
├── .gitignore                # Version Control Exclusion Rules
├── README.md                 # Technical Project Documentation
└── LICENSE                   # MIT Open-Source License
```

---

## Technology Stack

### Programming Language & Engine
- **Python 3.10+:** Core runtime environment.
- **Pygame 2.5+:** Multimedia cross-platform library for windowing, event handling, drawing, and timing.

### Architecture & Design Patterns
- **Object-Oriented Programming (OOP):** Modular class hierarchy for game entities.
- **Game Loop Pattern:** Frame-rate regulated update and render pipeline.
- **Particle System Architecture:** Vector-based short-lived particle rendering for visual feedback.

### Data Persistence
- **Python File I/O:** Lightweight local text file serialization for high-score retention.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sushantkothari/snake-arcade-python.git
cd snake-arcade-python
```

### 2. Set Up Virtual Environment

#### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

Execute the game from the root directory using any of the following standard methods:

### Standard Execution

```bash
python main.py
```

### Module Execution

```bash
python -m snake_game.main
```

### Windows Launcher

```bash
py main.py
```

### Direct Virtual Environment Execution (Windows)

```bash
.venv\Scripts\python.exe main.py
```

---

## Game Controls & Mechanics

### Keyboard Controls

| Key | Action |
| :--- | :--- |
| **Arrow Keys** | Steer Snake Direction (Up, Down, Left, Right) |
| **Space Bar** | Start Game / Restart Game after Game Over |
| **ESC Key** | Quit Game and Close Window |

### Game Rules & Mechanics
- **Food Consumables:** Standard food items increase score and grow the snake body length by one segment.
- **Power-Up Items:** Bonus items grant extra points and activate temporary special visual feedback.
- **Environmental Obstacles:** Higher levels spawn static obstacles; colliding with an obstacle or grid wall results in immediate game over.
- **Speed Scaling:** Game tick velocity automatically increases as levels progress.

---

## Quality Assurance & Testing

The code structure supports validation across multiple operational criteria:

- **Collision Boundary Tests:** Verification of grid border enforcement and self-intersection logic.
- **Input Edge-Case Prevention:** Validation that opposite-direction inputs within a single frame tick are ignored to prevent invalid self-collisions.
- **Persistence Verification:** Automated read/write validation checking `highscore.txt` creation, parsing, and modification safety.

---

## Future Roadmap

- **Sound FX Engine:** Integration of `pygame.mixer` audio effects for movement, food pickup, and collision events.
- **Global Leaderboard Integration:** REST API connectivity for sync-ing scores with a cloud database.
- **Custom Visual Themes:** Selectable skin themes (Arcade Neon, Classic Green, Retro Monochrome).
- **Autonomous AI Bot Mode:** Heuristic A* pathfinding / Reinforcement Learning bot demonstrating automated snake gameplay.

---

## License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## Author

**Sushant Kothari**  
AI / Machine Learning Engineer & Software Developer  
- **GitHub:** [https://github.com/sushantkothari](https://github.com/sushantkothari)  
- **Specializations:** Agentic AI • LLM Orchestration • Deep Learning • Computer Vision • Software Architecture
