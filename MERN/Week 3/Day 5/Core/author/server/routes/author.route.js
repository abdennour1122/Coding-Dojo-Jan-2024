const AuthorController = require('../controllers/author.controller');

module.exports=(app)=>{
    //get all
    app.get('/api/authors',AuthorController.findALL);
// create one
    app.post('/api/authors/new',AuthorController.create);
// update 
    app.patch('/api/authors/:id',AuthorController.update);
// get one
    app.get('/api/authors/:id',AuthorController.getOne);
// delete
    app.delete('/api/authors/delete/:id',AuthorController.delete);
}