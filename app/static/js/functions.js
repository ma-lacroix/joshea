async function manageDAGs(action) {
    const endpoints = {
        removeAll: '/d/remove_all',
        findAll: '/c/submit_new'
    };

    if (!endpoints[action]) {
        console.error('Invalid action:', action);
        return;
    }

    try {
        const response = await fetch(endpoints[action], {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });

        if (response.ok) {
            const result = await response.json();
            alert(action === 'removeAll'
                ? 'Successfully removed all DAGs! Bye bye: ' + JSON.stringify(result)
                : 'Look at all these amazing DAGs!!!: ' + JSON.stringify(result, null, 2));
            location.reload();
        } else {
            alert(`Failed to ${action}. Status: ` + response.status);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred: ' + error.message);
    }
}
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
async function handleNextDagRun(dag_name) {
    try {
        const response = await fetch(`/r/get_next_dag_run?name=${encodeURIComponent(dag_name)}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (response.ok) {
            const result = await response.json(); // Convert response to JSON
            alert('Starting: ' + JSON.stringify(result, null, 2));
            fetch('/u/execute_dag', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ dag_name: result.dag_name, id: result.next_run })
            });
        } else {
            alert(`Failed to fetch next DAG run: ${response.status}`);
        }
    } catch (error) {
        console.error('Error:', error);
        alert(`An error occurred: ${error.message}`);
    }
}
