import sqlite from 'better-sqlite3';

let db;

const db_init = () => {
    db = sqlite(':memory:');

    db.exec(`
    CREATE TABLE users (
        uid integer primary key,
        user string,
        pass string
    );

    INSERT INTO users (user, pass) VALUES
        ('melon', 'Hunter2'), ('web-admin', 'man_i_love_my_secure_app'),
        ('admin', 'admin'), ('flag-haver', 'COMP6443{SUBMIT_ME_TO_CTFD}')
    `);
};

const execute = (query, quiet=false) => {
    db || db_init();

    console.error(`[*] DEBUG: ${query}`);

    try {
        const result = db.prepare(query).get();
        if (result) return { success: true, data: result };
    } catch (e) {
        console.warn(`[-] ERROR: ${e.toString()}`);
        if (!quiet) return { success: false, data: e.toString() };
    }

    return { success: false, data: "Incorrect username or password" };
};

export default execute;
