# Tarea: Casos de uso de una biblioteca

## Especificaciones de casos de uso

  |  Caso de Uso	(CU) | Buscar libro (CU-1) |
  |---|---|
  | Actor  |  _Usuario_ |
  | Descripción | _El usuario busca un libro de interés_  |
  | Flujo básico | _CU-1_ |
  | Pre-condiciones | _No tiene_  |  
  | Post-condiciones  | _No tiene_  |  
  |  Requerimientos | _El libro debe existir_  |
  | Autor  | _Miguel Ángel García Rodríguez_ |
  |Fecha | _23/01/2024_ |

<br>

  |  Caso de Uso	(CU) | Devolver libro (CU-2) |
  |---|---|
  | Actor  |  _Usuario, Bibliotecario_ |
  | Descripción | _El usuario devuelve el libro que ha sido prestado por el bibliotecario_  |
  | Flujo básico | _CU-2_ |
  | Pre-condiciones | _No tiene_  |  
  | Post-condiciones  | _No tiene_  |  
  |  Requerimientos | _El libro debe el libro haber sido prestado primero_  |
  | Autor  | _Miguel Ángel García Rodríguez_ |
  |Fecha | _23/01/2024_ |

<br>

  |  Caso de Uso	(CU) | Prestar libro (CU-3) |
  |---|---|
  | Actor  |  _Usuario, Bibliotecario_ |
  | Descripción | _El usuario pide prestado un libro al biblliotecario_  |
  | Flujo básico | _CU-3_ |
  | Pre-condiciones |  _No tiene_ |  
  | Post-condiciones  | _El usuario debe de estar verificado (CU-4)_ |  
  |  Requerimientos |  |
  | Autor  | _Miguel Ángel García Rodríguez_ |
  |Fecha | _23/01/2024_ |

<br>

  |  Caso de Uso	(CU) | Verificar usuario (CU-4) |
  |---|---|
  | Actor  |  _Usuario, Bibliotecario_ |
  | Descripción | _Se verifica la identidad del usuario_  |
  | Flujo básico | _CU-3, CU-4_ |
  | Pre-condiciones | _El usuario debe de haber pedido prestado un libro (CU-3)_  |  
  | Post-condiciones  | _No tiene_  |  
  |  Requerimientos ||
  | Autor  | _Miguel Ángel García Rodríguez_ |
  |Fecha | _23/01/2024_ |

## Especificaciones de los actores

|  Actor | Bibliotecario (A-1) |
|---|---|
| Descripción  | _Actor que trabaja en una biblioteca_  |
| Características  | _Interactua con 3 Casos de Uso_ |
| Relaciones | _CU-2, CU-3, CU-4_ |
| Referencias | _CU-2, CU-3, CU-4_ |   
| Autor  | _Miguel Ángel García Rodríguez_ |
|Fecha | _23/01/2024_ |

<br>

|  Actor | Usuario (A-2) |
|---|---|
| Descripción  | _Actor que interactua con una biblioteca_ |
| Características  | _Interactua con 3 casos de uso_ |
| Relaciones | _Se relaciona con el actor 'Bibliotecario(A-1) en el caso de uso CU-3_  |
| Referencias | _CU-1, CU-2, CU-3, CU-4_ |   
| Autor  | _Miguel Ángel García Rodríguez_ |
|Fecha | _23/01/2024_ |