const fetch = require('node-fetch');

module.exports = {
    /**
     * Get an Duo OTP from server
     * @param {string} url URL to the server, ie http://localhost:9123
     * @param {string} userid ID to query server with
     * @param {string} userkey Optional encryption key
     * @return {string} OTP
     */
    getOTPFromServer: async (url, userid, userkey=null) => {
        const params = new URLSearchParams();
        params.append('userid', userid);
        if (userkey)
            params.append('userkey', userkey);

        const response = await fetch(url + '/get_otp', { method: 'POST', body: params });
        const data = await response.json();

        if (data.error)
            throw data.error;
        return data.otp;
    },

    /**
     * Update counter on a server
     * @param {string} url URL to the server, ie http://localhost:9123
     * @param {string} userid ID to query server with
     * @param {string} userkey Optional encryption key
     * @return {string} OTP
     */
    updateCounterFromServer: async (url, userid, userkey=null) => {
        const params = new URLSearchParams();
        params.append('userid', userid);
        if (userkey)
            params.append('userkey', userkey);
        const response = await fetch(url + '/inc_count', { method: 'POST', body: params });
        const data = await response.json();

        if (data.error)
            throw data.error;
        return data;
    },

    /**
     * Get an Duo OTP from a secret file. ONLY USE THIS IF THE DUO
     * BOT IS THE ONLY DEVICE USING THE SECRET.
     * @param {string} secretfile Path to secret file, see example secret file
     * @return {string} OTP
     */
    getOTPFromSecret: async secretfile => {

    }
};