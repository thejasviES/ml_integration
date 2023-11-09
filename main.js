const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
    const jsonData = JSON.parse(fs.readFileSync('temperature_data.json'));
    const jsonDataString = JSON.stringify(jsonData);

    const python = spawn('python', ['trainModel.py', jsonDataString]);

    python.stdout.on('data', function (data) {
        console.log('Pipe data from Python script ...');
    });


    python.on('close', (code) => {
        console.log(`Child process closed with code ${code}`);

    });

});

app.get("/predict", () => {

    const timestamp = "2023-01-01 09:23:17";

    const python = spawn('python', ['predict.py', timestamp]);
    python.stdout.on('data', (data) => {
        console.log(data.toString());
    });

})
app.listen(port, () => {
    console.log(`App listening on port ${port}!`);
});