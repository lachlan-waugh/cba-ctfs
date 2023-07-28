import express from 'express';
import cookieParser from 'cookie-parser'; 
import execute from './database.js';
import fs from 'fs';

const app = express();
const port = 3000;
app.use(express.json());
app.use(cookieParser());

const SECRET = "SECRET_PASSWORD_123";

app.get('/', (req, res) => {
    if (!req.cookies.token) return res.redirect('/login');

    const [ user, pass, secret ] = atob(req.cookies.token).split(':');

    if (secret === SECRET) { // why yes, security is my passion B)
        res.send(`welcome ${user}. Man, '${pass}' is a really strong password, well done!`);
    } else {
        res.redirect('/login');
    }
});

app.get('/login', (_, res) => res.end(fs.readFileSync('./site/login.html')));

app.post('/login', (req, res) => {
    const { user, pass, method } = req.body;

    // tried to use {...}[] ?? { ... }, but it kept breaking
    // TODO: maybe fix it later? idk
    const result = (method) ? {
        'btn1': () => execute(`SELECT user, pass FROM users WHERE user = '${user}' AND pass = '${pass}'`),
        'btn2': () => execute(`SELECT user, pass FROM users WHERE (user = '${user}' AND pass = '${pass}')`),
        'btn3': () => {
            let stripped_user = user;
            while (stripped_user.includes('OR')) stripped_user = stripped_user.replace(/OR/gi, '');
            return execute(`SELECT user, pass FROM users WHERE (user = '${stripped_user}' AND pass = '${pass}')`, true)
        },
        'btn4': () => {
            const res = execute(`SELECT user, pass FROM users WHERE user = '${user}' and pass = '${pass}'`);

            // I wanted to simulate an empty database, but couldn't be bothered
            // so instead: check the user doesn't exist, and fail if they do l0l
            // how do you bypass this check I wonder :thonking:
            return (execute(`SELECT user, pass FROM users WHERE user = '${res.data.user}' AND pass = '${res.data.pass}'`).success)
            ? { success: false, data: 'nah man that ain\'t it' }
            : res;
        }
    }[method]() : { success: false, data: 'nah man' };
 
    if (result.success) {
        // TEN LAYERS OF eNcRyPtIoN
        res.end(JSON.stringify({ success: true, data: btoa(`${result.data.user}:${result.data.pass}:${SECRET}`) }));
    } else {
        res.end(JSON.stringify(result));
    }
});

app.listen(port, () => console.log(`[*] listening on localhost:${port}`));
