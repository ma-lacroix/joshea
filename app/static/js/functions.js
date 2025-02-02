async function launchDAG(dag_name) {
    try {
        const response = await fetch('/c/schedule_dag_run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name: dag_name }) // Corrected JSON format
        });

        if (response.ok) {
            const result = await response.json();
            alert('Successfully scheduled a run for: ' + dag_name);
            location.reload();
        } else {
            alert('Failed to submit DAG. Status: ' + response.status);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    }
}
async function removeAll() {
    try {
        const response = await fetch('/d/remove_all', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (response.ok) {
            const result = await response.json();
            alert('Successfully removed all DAGs! Bye bye: ' + JSON.stringify(result));
            location.reload();
        } else {
            alert('Failed to remove. Status: ' + response.status);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    }
}
async function findAllDAGs() {
    try {
        const response = await fetch('/c/submit_new', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        if (response.ok) {
            const result = await response.json();
            alert('Look at all these amazing DAGs!!!: ' + JSON.stringify(result, null, 2));
            location.reload();
        } else {
            alert('Failed to fetch new DAGs. Status: ' + response.status);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    }
}