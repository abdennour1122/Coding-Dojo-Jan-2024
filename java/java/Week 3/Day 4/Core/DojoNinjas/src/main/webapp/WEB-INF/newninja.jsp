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
<title>Insert title here</title>
</head>
<body>
<div class="container mt-3">
        <h1>New Ninja</h1>
	<div>
		<form:form action="/processninja" method="POST" modelAttribute="ninja">

            <form:select path="mydojo">
                <c:forEach var="oneDojo" items="${dojos}">
            <!--- Each option VALUE is the id of the person --->
                    <form:option value="${oneDojo.id}" path="mydojo">
            <!--- This is what shows to the user as the option --->
                    <c:out value="${oneDojo.name}"/>
                    </form:option>
                </c:forEach>
            </form:select>

            <br>

			<form:label path="firstName" class="form-label">First Name</form:label>
			<form:input path="firstName" class="form-control"/>
			<form:errors class="text-danger" path="firstName"/>
			<br>

            <form:label path="lastName" class="form-label">Last Name</form:label>
			<form:input path="lastName" class="form-control"/>
			<form:errors class="text-danger" path="lastName"/>
			<br>

            <form:label path="age" class="form-label">Age</form:label>
			<form:input path="age" type="number"  class="form-control"/>
			<form:errors class="text-danger" path="age"/>
			<br>

			<div>
				<input type="submit" value="Create" class="btn btn-primary">
			</div>
		</form:form>
	</div>

</div>
</body>
</html>