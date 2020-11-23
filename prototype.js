const express=require("express");
const app=express();
const router=express.Router();
const mdb=require("mongodb").MongoClient;
const url="mongodb://localhost:27017";
const ops={useUnifiedTopology: true}
const dbname="last";
app.set("view engine","ejs");
app.use(express.urlencoded({extended:false}));
app.use(express.static("home"));
app.get("/",(request,response)=>response.render("index",{"title":"type:"}));

app.listen(3000);
