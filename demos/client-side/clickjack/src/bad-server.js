const express = require('express');
var cors = require('cors');

const app = express();
const port = 3001;

app.set('views', './views');
app.set('view engine', 'ejs');
app.use(cors());
app.use(express.static('public'));

app.get('/', (_, res) => res.render('index'));

app.listen(port, () => console.log(`[*] bad server listening on localhost:${port}`));