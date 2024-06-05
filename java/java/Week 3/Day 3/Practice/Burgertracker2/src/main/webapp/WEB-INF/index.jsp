<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page isErrorPage="true" %> <!--This line is added to display the error page  -->
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="/css/style.css">
<title>Burger</title>
</head>
<body>
    <div class="container center-container">
        <div class="content">
            <h1>Burger Tracker</h1>
            <table class="table table-bordered">
                <thead>
                    <tr class="table-secondary">
                        <th>Burger Name</th>
                        <th>Restaurant Name</th>
                        <th>Rating (out of 5)</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach var="burger" items="${burgers}">
                        <tr>
                            <td>${burger.burgerName}</td>
                            <td>${burger.restaurantName}</td>
                            <td>${burger.rating}</td>
                            <td>
                                <a href="/edit/${burger.id}" class="btn btn-primary">Edit</a>
                            </td>
                        </tr>
                    </c:forEach>
                </tbody>
            </table>
        </div>
        
        <div class="content2">
            <h2>Add a Burger:</h2>
            <form:form action="/create" method="post" modelAttribute="burger" >
                <p class="form-group d-flex">
                    <form:label path="burgerName" class="col-form-label text-nowrap me-5">Burger Name:</form:label>
                    <form:errors path="burgerName" cssClass="text-danger text-nowrap"/>
                    <form:input path="burgerName" class="form-control"></form:input>
                </p>
                <p class="form-group d-flex">
                    <form:label path="restaurantName" class="col-form-label text-nowrap me-4">Restaurant Name:</form:label>
                    <form:errors path="restaurantName" cssClass="text-danger text-nowrap"/>
                    <form:input path="restaurantName" class="form-control"></form:input>
                </p>
                <p class="form-group d-flex">
                    <form:label path="rating" class="col-form-label text-nowrap me-5">Rating:</form:label>
                    <form:errors path="rating" cssClass="text-danger text-nowrap"/>
                    <form:input path="rating" class="form-control ms-5"></form:input>
                </p>
                <p class="form-group d-flex">
                    <form:label path="notes" class="col-form-label text-nowrap me-5">Notes:</form:label>
                    <form:errors path="notes" cssClass="text-danger text-nowrap"/>
                    <form:textarea path="notes" class="form-control ms-5"></form:textarea>
                </p>
                <div class="text-end">
                    <input type="submit" class="btn btn-primary" value="Submit"/>
                </div>
            </form:form>
        </div>
    </div>

</body>
</html>