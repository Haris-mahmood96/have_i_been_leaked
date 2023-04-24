db.createUser({
    user: 'osint',
    pwd: 'osint',
    roles: [
        {
            role: 'readWrite',
            db: 'social_media_osint_db',
        },
    ],
});
