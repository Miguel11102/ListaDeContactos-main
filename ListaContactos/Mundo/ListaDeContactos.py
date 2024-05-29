from Mundo.Contacto import Contacto

class ListaDeContactos:
    def __init__(self):
        self.contactos = []

    def darTodosLosContactos(self):
        return [contacto.darNombre() + " " + contacto.darApellido() for contacto in self.contactos]

    def buscarContactosPalabraClave(self, palabra):
        resultado = []
        for contacto in self.contactos:
            if contacto.contienePalabraClave(palabra) or palabra in contacto.darNombre() or palabra in contacto.darApellido():
                resultado.append(contacto.darNombre() + " " + contacto.darApellido())
        return resultado

    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos: 
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) is not None:
            return False
        nuevo_contacto = Contacto(nombre, apellido, direccion, correo)
        for telefono in telefonos:
            nuevo_contacto.agregarTelefono(telefono)
        for palabra in palabras:
            nuevo_contacto.agregarPalabra(palabra)
        self.contactos.append(nuevo_contacto)
        return True

    def eliminarContacto(self, nombre, apellido):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto is None:
            return False
        self.contactos.remove(contacto)
        return True

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        contacto = self.buscarContacto(nombre, apellido)
        if contacto is None:
            return False
        contacto.cambiarDireccion(direccion)
        contacto.cambiarCorreo(correo)
        self.actualizarTelefonos(telefonos, contacto)
        self.actualizarPalabras(palabras, contacto)
        return True

    def actualizarTelefonos(self, telefonos, contacto):
        contacto.telefonos = telefonos

    def actualizarPalabras(self, palabras, contacto):
        contacto.palabras = palabras

    def metodo1(self):
        pass

    def metodo2(self):
        pass