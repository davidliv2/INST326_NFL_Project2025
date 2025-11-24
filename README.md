# NFL Analytics System - Project 3

**INST326 Advanced OOP with Inheritance & Polymorphism**  
*Student: David, Andrew, Dash 

---

##Project Overview

This NFL Analytics System demonstrates advanced Object-Oriented Programming concepts including inheritance hierarchies, polymorphic behavior, abstract base classes, and composition relationships. The system analyzes NFL player performance data and provides team rankings and statistical insights.

### Key Features
- **Inheritance Hierarchy**: Player base class with specialized offensive, defensive, and special teams subclasses
- **Polymorphism**: Different efficiency calculation methods for each player type
- **Abstract Base Classes**: Enforced interface contracts using Python's ABC module
- **Composition**: Teams contain players and season statistics
- **Analytics Engine**: Polymorphic ranking and comparison tools

---

## 📋 Project Requirements Met

**Inheritance Hierarchy** - Player base class with 3 derived classes  
**Abstract Base Classes** - ABC module with abstract methods  
**Polymorphism** - Method overriding with different behaviors  
**Composition** - Team "has-a" Players and SeasonStats  
**Code Quality** - Clean code with type hints and documentation  
**Testing** - Comprehensive test suite covering all OOP concepts  

---

## Architecture Overview

### Class Hierarchy Diagram

```
Abstract Player
    │
    ├── OffensivePlayer (QB, RB, WR, TE)
    │   ├── efficiency_score() → yards + touchdowns / games
    │   └── get_primary_stats() → total_yards, touchdowns, yards_per_game
    │
    ├── DefensivePlayer (DL, LB, CB, S)
    │   ├── efficiency_score() → tackles + sacks + INTs / games
    │   └── get_primary_stats() → tackles, big_plays, tackles_per_game
    │
    └── SpecialTeamsPlayer (K, P, Return)
        ├── efficiency_score() → FGs + punts + return_TDs / games
        └── get_primary_stats() → FG%, return_TDs, punts_inside_20

Composition Relationships:
Team ──contains──> List[Player]
Team ──contains──> SeasonStats
StatsDataset ──contains──> DataFrame
```

### Polymorphism in Action

All player types implement the same interface but with different behavior:

```python
# Same method call, different calculations based on player type
for player in mixed_roster:
    score = player.efficiency_score()  # Polymorphic behavior!
    stats = player.get_primary_stats()  # Different stats per type
```

---

## Installation and Usage

### Prerequisites
```bash
pip install pandas
```

### Basic Usage

```python
from nfl_analytics_improved import *

# Create sample data
df = create_sample_data()
dataset = StatsDataset(df)

# Build team rosters
bills = dataset.build_team_roster("BUF")
rams = dataset.build_team_roster("LAR")

# Demonstrate polymorphism
print("Player Efficiency Scores:")
for player in bills.roster:
    print(f"{player.name} ({player.position}): {player.efficiency_score():.2f}")

# Analytics with polymorphic behavior
all_players = bills.roster + rams.roster
rankings = AnalyticsEngine.rank_players(all_players)
print(rankings)
```

### Advanced Features

```python
# Team composition examples
team = Team("Buffalo Bills", "BUF")
team.add_player(qb_player)
team.season_stats.add_game_result(31, 10)  # Win by 21

# Position-specific analysis
qb_rankings = AnalyticsEngine.compare_positions(all_players, "QB")
team_analysis = AnalyticsEngine.team_position_analysis(bills)
```

---

## Testing

Run the comprehensive test suite:

```bash
python test_nfl_analytics.py
```

### Test Coverage

The test suite covers all OOP concepts:

- **Inheritance Tests**: Verify proper parent-child relationships
- **Abstract Class Tests**: Ensure abstract methods are enforced
- **Polymorphism Tests**: Confirm different behavior for same interface
- **Composition Tests**: Validate "has-a" relationships
- **Integration Tests**: End-to-end functionality testing

---

## 📊 Examples of OOP Concepts

### 1. Inheritance Example

```python
# All player types inherit from Player base class
qb = OffensivePlayer("Josh Allen", "BUF", "QB", passing_yards=4000)
lb = DefensivePlayer("Matt Milano", "BUF", "LB", tackles=100)

# Both inherit common methods and attributes
print(qb.name)  # Inherited from Player
print(lb.team)  # Inherited from Player
print(qb.summary_row())  # Inherited method
```

### 2. Polymorphism Example

```python
players = [
    OffensivePlayer("QB1", "BUF", "QB", touchdowns=30, games_played=16),
    DefensivePlayer("LB1", "BUF", "LB", sacks=10, games_played=16), 
    SpecialTeamsPlayer("K1", "BUF", "K", field_goals_made=25, games_played=16)
]

# Same method call, different behavior based on object type
for player in players:
    score = player.efficiency_score()  # Different calculation for each type
    print(f"{player.position}: {score}")
```

**Output:**
```
QB: 15.0   # (30 touchdowns * 6) / 16 games = 11.25 + other stats
LB: 1.875  # (10 sacks * 3) / 16 games = 1.875
K: 3.125   # (25 FGs * 2) / 16 games = 3.125
```

### 3. Abstract Base Class Example

```python
from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def efficiency_score(self) -> float:
        pass  # Must be implemented by all subclasses

# This will raise TypeError:
try:
    generic_player = Player("Test", "BUF", "XX")
except TypeError:
    print("Cannot instantiate abstract class!")
```

### 4. Composition Example

```python
# Team HAS players (composition, not inheritance)
team = Team("Buffalo Bills", "BUF")
team.add_player(qb_player)  # Team contains players
team.add_player(rb_player)

# Team HAS season statistics
team.season_stats.add_game_result(28, 21)  # Team contains stats
print(f"Record: {team.season_stats}")

# Why not inheritance? Team is not a TYPE of Player!
# Team contains many players - this is composition
```

---

## 🎯 Key Design Decisions

### Inheritance vs Composition

**Used Inheritance For:**
- Player specialization (QB IS-A Player, LB IS-A Player)
- Common interface with specialized behavior
- Code reuse for shared attributes

**Used Composition For:**
- Team roster management (Team HAS Players)
- Season statistics (Team HAS SeasonStats)
- Data storage (Dataset HAS DataFrame)

### Why Abstract Base Classes?

```python
class Player(ABC):
    @abstractmethod
    def efficiency_score(self) -> float:
        """Must be implemented - different for each position"""
        pass
```

**Rationale:**
- A generic "Player" without position doesn't make sense
- Forces all subclasses to implement position-specific calculations
- Provides interface contract for polymorphic behavior
- Compile-time checking of required methods

---

## 📁 File Structure

```
project-repo/
│
├── nfl_analytics_improved.py     # Main system implementation
├── test_nfl_analytics.py         # Comprehensive test suite
├── README.md                     # This file
├── docs/
│   └── Architecture_Document.md  # Detailed design documentation
└── sample_data.csv              # Example NFL player data
```

---

## Future Enhancements

Potential extensions that demonstrate OOP principles:

1. **Additional Player Types**: 
   ```python
   class CoachingStaff(Player):  # New inheritance branch
       def efficiency_score(self) -> float:
           return self.wins / self.games_coached
   ```

2. **Advanced Composition**:
   ```python
   class League:
       def __init__(self):
           self.teams: List[Team] = []      # League HAS teams
           self.schedule: Schedule = []     # League HAS schedule
   ```

3. **Strategy Pattern**:
   ```python
   class EfficiencyCalculator(ABC):
       @abstractmethod
       def calculate(self, stats) -> float: pass
   
   class ModernOffenseCalculator(EfficiencyCalculator): pass
   class TraditionalOffenseCalculator(EfficiencyCalculator): pass
   ```

---

## Learning Objectives Achieved

- **Inheritance**: Proper parent-child relationships with method overriding
- **Polymorphism**: Same interface, different behavior based on object type
- **Abstract Classes**: Interface contracts enforced at compile time
- **Composition**: "Has-a" relationships modeling real-world structures
- **Design Patterns**: Factory method, implicit strategy pattern
- **Clean Code**: Type hints, documentation, error handling


**Key Learning Points:**
- When to use inheritance vs composition
- How polymorphism enables flexible, extensible code
- Why abstract base classes provide better interface contracts
- How proper OOP design makes code more maintainable



