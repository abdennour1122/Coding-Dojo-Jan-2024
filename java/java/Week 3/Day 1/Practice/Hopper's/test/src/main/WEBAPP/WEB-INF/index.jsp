<%@ taglib prefix="c" uri="http://java.sun.com/jstl/core" %>
<%--
  Created by IntelliJ IDEA.
  User: najem
  Date: 24/05/2024
  Time: 15:16
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Item Details</title>
</head>
<body>
<h1><c:out value="${itemName}"/></h1>
<p>Price: <c:out value="${price}"/></p>
<p>Description: <c:out value="${description}"/></p>
<p>Vendor: <c:out value="${vendor}"/></p>
</body>
</html>