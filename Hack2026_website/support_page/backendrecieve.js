//connecting to database  
const express = require("express");
const { MongoClient } = require("mongodb");

const app = express();
const client = new MongoClient("mongodb+srv://jonathansandjong_db_user:"); 
 
let db;

async function start() {
    await client.connect();
    db = client.db("myDatabase"); //name must be changed to match database
    app.listen(3000);
}

start();

///when requests happen
app.get("/users", async (req, res) => {
    const users = await db.collection("users").find().toArray(); //users to be changed?
    res.json(users);
});

await db.collection("mangodata").find(query).toArray()