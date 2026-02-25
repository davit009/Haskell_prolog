% Pequeño sistema experto (diagnóstico médico)
% Archivo solicitado: experto.pl

:- dynamic sintoma/1.

medicamento(paracetamol) :- sintoma(fiebre), sintoma(dolor).
medicamento(loratadina) :- sintoma(alergia), sintoma(estornudos).
medicamento(jarabe) :- sintoma(tos), sintoma(garganta).

recomendacion(M) :- medicamento(M), !.
recomendacion(observacion_y_consulta).
