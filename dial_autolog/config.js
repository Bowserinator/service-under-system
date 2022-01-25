// use either server or self login or autoclick push
// chrome/firefox path

module.exports = {
    loginMethod: 'server', // push | server | secret 
    loginCredentials: {
        secretsFile: '/path/to/secrets.hotp',   // if loginMethod=secret
        serverAddress: 'http://localhost:9123', // if loginMethod=server
        userid: 'duotoken',                     // if loginMethod=server
        userkey: 'optional encryption key',     // if loginMethod=server
    }
};
