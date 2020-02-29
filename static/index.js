$(document).ready(function () {

    const context = document.getElementById('canvas').getContext('2d');
    const chart = new Chart(context, config);
    const source = new EventSource("/test");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        console.log(data);
        if (config.data.labels.length === 20) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
        }
        config.data.labels.push(data.key);
        config.data.datasets[0].data.push(data.value);
        // data.value.forEach(function (item) {
        //     config.data.datasets[0].data.push(item);
        //     console.log(item);
        // });
        chart.update();
    }
});

