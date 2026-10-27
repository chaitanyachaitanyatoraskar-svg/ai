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
