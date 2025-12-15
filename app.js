const express = require('express');
const mongoose = require('mongoose');

const app = express();

mongoose.connect('mongodb://mongo:27017/testdb');

app.get('/', (req, res) => {
  res.send("CI/CD Pipeline with Jenkins, Docker & Kubernetes");
});

app.listen(3000, () => {
  console.log("App running on port 3000");
});
