new Vue ({
el: '#get_user',
data: {
    result: []
},
methods : {
    get_username: function (username) {
        const data = new FormData();
        data.append("user", String(username));
        axios.post('/home/tabs/', data)
    }
}
})
