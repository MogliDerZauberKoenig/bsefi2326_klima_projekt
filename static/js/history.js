let labels = ['18.11.24', '19.11.24', '20.11.24', '21.11.24', '22.11.24'];
let dataset1Data = [10, 25, 13, 18, 30];
let dataset2Data = [20, 15, 28, 22, 10];

let ctx = document.getElementById('testChart').getContext('2d');
let myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [
            {
                label: 'Soll',
                data: dataset1Data,
                borderColor: 'blue',
                borderWidth: 2,
                fill: false,
            },
            {
                label: 'Ist',
                data: dataset2Data,
                borderColor: 'red',
                borderWidth: 2,
                fill: false,
            }
        ]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Datum',
                    font: {
                        padding: 4,
                        size: 20,
                        weight: 'bold',
                        family: 'Arial'
                    },
                    color: 'darkblue'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Temperatur',
                    font: {
                        size: 20,
                        weight: 'bold',
                        family: 'Arial'
                    },
                    color: 'darkblue'
                },
                beginAtZero: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Values',
                }
            }
        }
    }
});