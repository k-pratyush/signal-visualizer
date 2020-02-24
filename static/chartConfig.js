const config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: "Uni-polar",
            backgroundColor: 'rgb(255, 99, 132)',
            borderColor: 'rgb(255, 99, 132)',
            data: [],
            fill: false,
            borderWidth: 2,
            steppedLine: true,
            fill: false
        }],
    },
    options: {
        responsive: true,
        title: {
            display: true,
            text: 'Real time chart'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        },
        hover: {
            mode: 'nearest',
            intersect: true
        },
        scales: {
            xAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Bits'
                }
            }],
            yAxes: [{
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Amplitude'
                }
            }]
        }
    }
};
