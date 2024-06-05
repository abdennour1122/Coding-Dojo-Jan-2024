<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true"%>
<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<!-- <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" /> -->

<%@ taglib prefix = "fmt" uri = "http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<link rel="stylesheet" type="text/css" href="/css/style.css">
<title>Insert title here</title>
</head>
<body>
    <div class="container center-container">
        <div class="content">
            <h1>Save Travels</h1>
            <table class="table table-bordered">
                <thead>
                    <tr class="table-secondary">
                        <th>Expense</th>
                        <th>Vendor</th>
                        <th>Amount</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <c:forEach var="expense" items="${allExpense}">
                        <tr>
                            <td><a href="/expense/${expense.id}">${expense.name}</a></td>
                            <td>${expense.vendor}</td>
                            <td>${expense.amount}</td>
                            <td class="d-flex justify-content-around align-items-center">
                                <a href="/edit/${expense.id}">Edit</a>
                                <a href="/delete/${expense.id}" class="btn btn-danger" >Delete</a>
                            </td>
                        </tr>
                    </c:forEach>
                </tbody>
            </table>
        </div>
        
        <div class="content2">
            <h2>Add an expense:</h2>
            <form:form action="/create" method="post" modelAttribute="expense" class="form " >
                <p class="form-group para">
                    <form:label path="name" class="col-form-label text-nowrap  label">Expense Name:</form:label>
                    <form:errors path="name" cssClass="text-danger text-nowrap"/>
                    <form:input path="name" class="form-control input"></form:input>
                </p>
                <p class="form-group para">
                    <form:label path="vendor" class="col-form-label text-nowrap  label">Vendor:</form:label>
                    <form:errors path="vendor" cssClass="text-danger text-nowrap"/>
                    <form:input path="vendor" class="form-control input"></form:input>
                </p>
                <p class="form-group para">
                    <form:label path="amount" class="col-form-label text-nowrap  label">Amount:</form:label>
                    <form:errors path="amount" cssClass="text-danger text-nowrap"/>
                    <form:input path="amount" class="form-control input"></form:input>
                </p>
                <p class="form-group para">
                    <form:label path="description" class="col-form-label text-nowrap  label">Description:</form:label>
                    <form:errors path="description" cssClass="text-danger text-nowrap"/>
                    <form:textarea path="description" class="form-control input"></form:textarea>
                </p>
                <div class="d-flex justify-content-end">
                    <input type="submit" class="btn btn-primary" value="Submit"/>
                </div>
            </form:form>
        </div>
    </div>
</body>
</html>