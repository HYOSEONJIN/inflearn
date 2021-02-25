const express = require('express')
const app = express()
const port = 3000

const {user, User} = require("./models/User");

const bodyParser = require('body-parser');
//application/x-www/-fom-urlencoded
app.use(bodyParser.urlencoded({extended:true}));
//application/json
app.use(bodyParser.json());

const mongoose = require('mongoose')
mongoose.connect('mongodb+srv://HYOSEON:adad11@hyseonbolierplate.9vvek.mongodb.net/myFirstDatabase?retryWrites=true&w=majority',{
    useNewUrlParser: true, useUnifiedTopology:true, useCreateIndex:true, useFindAndModify :false
}).then(() => console.log('mongoDB Connected..'))
 .catch(err => console.log(err))

app.get('/', (req, res) => {  res.send('Hello World!')})


app.post('/register', (req, res) => {
 
    // 회원가입할 때 필요한 정보들을 클라이언트에서 가져오면
    // 그것들을 db에 넣어준다


    const user = new User(req.body)

    user.save((err, userInfo) =>{
        if(err) return res.json({success :false, err})
        return res.status(200).json({success : true
        })
    })
})

app.listen(port, () => {  console.log(`Example app listening at http://localhost:${port}`)})