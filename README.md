# Qiskit Fall Fest 2025
This repository contains code examples and tutorials for the Kipu Quantum Hub as part of the Qiskit Fall Fest 2025.

Some important links for the session:
- [Kipu Quantum Hub](https://hub.kipu-quantum.com/): The Kipu Quantum Hub platform where you can deploy and run quantum services.
- [Quantum Hub Documentation](https://docs.hub.kipu-quantum.com/): Documentation for the Kipu Quantum Hub and its SDKs.

## Repository Structure
- `notebooks/`: Contains Jupyter notebooks with code examples demonstrating how to use the Kipu Quantum Hub with our SDKs.
- `src/`: Contains the source code for a service that is ready to be deployed on the Kipu Quantum Hub.

## Set up the Environment

We recommend creating a dedicated Python environment to install and track all required packages from the start.
You may use the `requirements.txt` file to create a virtual environment with the tooling of your choice.
In the following, we use [`uv`](https://github.com/astral-sh/uv) to create a new virtual environment and install the required packages:

```bash
uv venv
uv sync

source .venv/bin/activate
```

You can use the following command to update the dependencies and the `uv.lock` file:

```bash
uv sync -U
```

If you are using `uv`, you have to update the requirements files after installing new packages:

```bash
uv export --format requirements-txt --no-dev --no-emit-project > requirements.txt
uv export --format requirements-txt --only-dev --no-emit-project > requirements-dev.txt
```

## Running the service 

### Run the code

You can run the code by executing the following command:

```bash
python -m src
```

By this, the `src` folder is executed as a Python module and the `__main__.py` is executed.
The `__main__.py` is prepared to read the input data from the `input` directory and to call the `run()` method of `program.py`.

**This is helpful for local testing.**
Locally, you can test your code with a JSON-conform input that gets imported within the `__main__`-method.
You can use the files in the `input` folder to provide the required input data for your service.
You may adjust the `__main__`-method, for example, to load a different set of input from the `input` folder or to execute the
`run()` method with some static input.

## Using PLANQK CLI to deploy your service
You can install the CLI via npm:

```bash
npm install -g @planqk/planqk-cli
```

Login to your account using [your access token](https://dashboard.hub.kipu-quantum.com/home):

```bash
planqk login -t <your access token>
```

Use `planqk serve` to run your project locally and expose it through a local web server, similarly to how the Quantum Hub would run your code.
The local web server exposes the same HTTP endpoints to start a service execution, to check the status of running executions, to cancel executions, and to retrieve execution results.

Use `planqk up` to deploy your service to the PLANQK Platform.
Next, you may use `planqk run` to execute your service.
For more information, see the [PLANQK documentation](https://docs.planqk.de/quickstart.html).

As soon as the service is ready to use, you will be able to run Jobs to execute your service.
Further, you may publish it for internal use or into the Quantum Hub Marketplace to share it with other users.