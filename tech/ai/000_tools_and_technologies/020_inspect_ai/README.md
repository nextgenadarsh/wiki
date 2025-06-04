Inspect AI
---

- An open-source framework for large language `model evaluations`
- Components of inspect evaluations:
    - Datasets
        - Contain a `set of labelled samples`.
        - Typically just a table with input and target columns, where input is a prompt and target is either literal value(s) or grading guidance.
    - Solvers
        - `Chained together to evaluate` the input in the dataset and `produce a final result`.
        - For example; A basic solver, `generate()`, just calls the model with a prompt and collects the output.
        - Other solvers might do prompt engineering, multi-turn dialog, critique, or provide an agent scaffold.
    - Scorers
        - Evaluate the `final output of solvers`.
        - They may use text comparisons, model grading, or other custom schemes

> References:

- [Inspect AI](https://inspect.aisi.org.uk/)
