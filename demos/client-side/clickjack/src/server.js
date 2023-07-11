const express = require("express");
const session = require('express-session');
const bodyParser = require('body-parser');

const port = 3000;
const app = express();

app.set('views', './templates');
app.set('view engine', 'ejs');

app.use(express.static('public'));
app.use(session({
  secret: 'really-cool-secret',
  resave: true,
  saveUninitialized: true,
  cookie: {
    httpOnly: true
  }
}));
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) =>
	res.render('index', { is_valid: req.session.is_valid, username: req.session.username })
);

app.get('/login', (req, res) => {
  req.session.is_valid = true;
  req.session.username = 'Melon';
  req.session.email = 'melon@coolmathgames.com';
  res.redirect('/');
});

app.post('/purchase', (req, res) => {
  console.log('[*] purchase has been made $$$.');
  (req.session.is_valid)
  ? res.render('index', { is_valid: req.session.is_valid, username: req.session.username, success: true })
  : res.redirect('/')
});

app.listen(port, () => console.log(`[*] bookstore server listening on localhost:${port}`));

