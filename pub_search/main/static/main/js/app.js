new Vue({
  el: '#add_article',
  data: {
  result: []
  },
  methods: {
    add: function (elements) {
      const data = new FormData();
      data.append("user", String(elements[0]));
      data.append("title", String(elements[1]));
      data.append("source", String(elements[2]));
      data.append("preprint", String(elements[3]));
      data.append("copy", String(elements[4]));
      data.append("authors",String(elements[5]));
      axios.post('/home/parser/add/',data)
      .then(function (response){
      console.log(response);
      })
    }
  }
})