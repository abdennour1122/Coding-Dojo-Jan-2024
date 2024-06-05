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
<link rel="stylesheet" type="text/css" href="/css/show.css">
</head>
<body>
<div class="container mt-3 center-container">
    <div class="d-flex justify-content-between align-items-center">
        <h1>Expense Details</h1>
        <a href="/expenses">Go back</a>
    </div>
    <div class="reservoir">
        <div class="d-flex justify-content-between align-items-center">
            <p>Expense Name: </p>
            <p>${expense.name}</p>
        </div>
        <div class="d-flex justify-content-between align-items-center">
            <p>Expense Description: </p>
            <p>${expense.description}</p>
        </div>
        <div class="d-flex justify-content-between align-items-center">
            <p>Vendor: </p>
            <p>${expense.vendor}</p>
        </div>
        <div class="d-flex justify-content-between align-items-center">
            <p>Amount Spent: </p>
            <p>${expense.amount}</p>
        </div>
    </div>
</div>
</body>
</html>