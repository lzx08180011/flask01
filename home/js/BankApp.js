let data={
    banks: []
};


let vm = new Vue({
    el:'#bank-app',
    data,
    mounted(){
        fetch('http://localhost:5000/bank')
        .then(resp=> resp.json())
        .then(data=>{
            for(i in data.data){
                this.banks.push(data.data[i])
        }
        })
    },
});