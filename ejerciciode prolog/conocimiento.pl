% Base de conocimiento para agente conversacional
:- dynamic nombre/2.
:- dynamic le_gusta/2.

registrar_nombre(Usuario, Nombre) :- assertz(nombre(Usuario, Nombre)).
registrar_gusto(Persona, Cosa) :- assertz(le_gusta(Persona, Cosa)).

quien_gusta(Cosa, Quien) :- le_gusta(Quien, Cosa).
