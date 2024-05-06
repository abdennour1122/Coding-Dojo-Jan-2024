const {Author} = require('../models/author.model')




// GET ALL THE AUTHORS
module.exports.findALL = (req,res)=>{
    Author.find({})
    .then ((obj=>res.json(obj)))
    .catch ((err)=>res.json(err))
};

// CREATE 
module.exports.create=(req,res)=>{
    Author.create(req.body)
    .then((obj=>res.json(obj)))
    .catch(err=> res.status(400).json(err))
};


// UPDATE 
module.exports.update=(req,res)=>{
    Author.findOneAndUpdate({_id:req.params.id},req.body,{new:true, runValidators:true})
    .then ((obj=>res.json(obj)))
    .catch(err=> res.status(400).json(err))
};

// GET ONE 
module.exports.getOne=(req,res)=>{
    Author.findOne({_id:req.params.id})
    .then((obj=>res.json(obj)))
    .catch(err=>res.json(err))
};

// DELETE 
module.exports.delete=(req,res)=>{
    Author.deleteOne({_id:req.params.id})
    .then((obj=>res.json(obj)))
    .catch(err=>res.json(err))
};