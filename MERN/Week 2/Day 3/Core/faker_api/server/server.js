const express=require('express')
const app = express()

const { faker } = require('@faker-js/faker');

const createUser=()=>{
    const user = {
        password: faker.internet.password(),
        email: faker.internet.email(),
        number : faker.number.int(29999999),
        firstName: faker.person.firstName(),
        lastName: faker.person.lastName(),
        _id : faker.string.uuid()
        };
    return user;
} 

const createCompany = () => {
    const company = {
        _id : faker.string.uuid(),
        name: faker.company.name(),
        address : {
        street : faker.location.street(),
        city : faker.location.city(),
        state : faker.location.state(),
        zipCode : faker.location.zipCode(),
        country : faker.location.country()
        }

        };
    return company;
};

app.use( express.json() );
app.use( express.urlencoded({ extended: true }) );


// ! test route
app.get('/' , (req , res) => {
    res.json({message : "server is running " })
})

app.post('/api/users/new', (req, res) => {
    req.body = createUser()
    res.status(201).json({ newUser: req.body})
})

app.post(`/api/companies/new` , (req , res) => {
    req.body = createCompany()
    res.status(201).json({ newCompany : req.body })
})

app.post(`/api/user/company` , (req , res) => {
    res.status(201).json({  newUser : createUser() ,newCompany : createCompany() })
})

app.listen(8000 , () => {
    console.log("http://localhost:8000/")
    console.log('server is  running  on port 8000');
})


