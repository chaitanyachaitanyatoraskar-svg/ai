# Practical 9: Posterior probability using Bayesian Networks (Burglar|Alarm=True)

## 📌 Problem Statement / Aim
Constructing a Bayesian network with Tabular CPDs and performing exact probabilistic inference using Variable Elimination with pgmpy.

## 💻 Source Code
File: [`posterior_probability_bayesian_networks.py`](./posterior_probability_bayesian_networks.py)

```python
# ==============================================================================
# Practical 9: Posterior probability using Bayesian Networks (Burglar|Alarm=True)
# Required: pip install pgmpy
# ==============================================================================

try:
    from pgmpy.models import DiscreteBayesianNetwork
except ImportError:
    from pgmpy.models import BayesianNetwork as DiscreteBayesianNetwork

from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = DiscreteBayesianNetwork([('Burglary', 'Alarm')])

# P(Burglary)
cpd_b = TabularCPD('Burglary', 2, [[0.99], [0.01]])

# P(Alarm | Burglary)
cpd_a = TabularCPD('Alarm', 2,
                   [[0.99, 0.1],
                    [0.01, 0.9]],
                   evidence=['Burglary'],
                   evidence_card=[2])

model.add_cpds(cpd_b, cpd_a)

# Find P(Burglary | Alarm=True)
infer = VariableElimination(model)
result = infer.query(['Burglary'], evidence={'Alarm': 1})

print(result)
```

## 🖥️ How to Run
```bash
python3 posterior_probability_bayesian_networks.py
```

## 📊 Expected Output (From Lab Manual)
```text
Output:
+-------------+---------------------+
| Burglary    | phi(Burglary)       |
+=============+=====================+
| Burglary(0) | 0.5238              |
+-------------+---------------------+
| Burglary(1) | 0.4762              |
+-------------+---------------------+
```
