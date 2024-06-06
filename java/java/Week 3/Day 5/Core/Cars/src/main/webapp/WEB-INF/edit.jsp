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
	<h1>Update ${car.model }</h1>
	<form:form action="/updateCar/${car.id}" method="post" modelAttribute="car">
		<input type="hidden" name="_method" value="put"/>
	
		<form:label path="model" class="form-label">Model</form:label>
		<form:input path="model" class="form-control"/>
		<form:errors class="text-danger" path="model"/>
		<br>
		<form:label path="color" class="form-label">Color</form:label>
		<form:input path="color" class="form-control"/>
		<form:errors class="text-danger" path="color"/>
		<br>
		<form:label path="price" class="form-label">Price</form:label>
		<form:input path="price" type="number" step="0.001" class="form-control"/>
		<form:errors class="text-danger" path="price"/>
		<br>
		<form:label path="releaseDate" class="form-label">Release Date</form:label>
		<form:input path="releaseDate" type="date" class="form-control"/> 
		<form:errors class="text-danger" path="releaseDate"/>
		<br>
		<div class="d-flex justify-content-between">
		<a class="btn btn-danger" href="/cars">Cancel</a>
		<input type="submit" value="Create" class="btn btn-sucess">
		</div>
		
		
			
	</form:form>
</div>
</body>
</html>