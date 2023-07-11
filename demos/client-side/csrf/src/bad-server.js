import express from 'express';
import exphbr from 'express-handlebars';

const bad_app = express();

bad_app.engine('html', exphbr.engine({
	defaultLayout: 'main',
	extname: '.html'
}));
bad_app.set('view engine', 'html');

bad_app.get('/', (_, res, next) => res.render('evil/index'));

bad_app.get('/clickme', (_, res, next) => res.render('evil/clickme'));

bad_app.get('/post', (_, res, next) => res.render('evil/post'));

bad_app.get('/form', (_, res, next) => res.render('evil/form'));

bad_app.listen(3001, () => console.log('bad server listening @ localhost:3001'));