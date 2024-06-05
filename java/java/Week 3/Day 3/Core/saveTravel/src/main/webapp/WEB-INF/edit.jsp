<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true"%>
<!-- for Bootstrap CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<%-- <link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" /> --%>

<%@ taglib prefix = "fmt" uri = "http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<div class="container mt-3">
    <div class="d-flex justify-content-between align-items-center">
    <h2>Edit Expense:</h2>
    <a href="/expenses" >Go back</a>
    </div>
    
    <form:form action="/update/${expense.id}" method="post" modelAttribute="expense" class="form " >
            <input type="hidden" name="_method" value="PUT"/>
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
</body>
</html>