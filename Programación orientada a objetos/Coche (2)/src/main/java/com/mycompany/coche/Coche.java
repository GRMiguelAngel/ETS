/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.coche;

/**
 *
 * @author grmiguelangel
 */
public class Coche {
    String color;
    String marca;
    String modelo;
    int cilindrada;
    
    public void arrancar(){
            System.out.println("Estoy arrancando");
    }
    public void acelerar(){
            System.out.println("Estoy acelerando");
    }       
    public void frenar(){
            System.out.println("Estoy frenando");
    }
    
    public static void main(String[] args) {
        Coche coche1 = new Coche();
        coche1.color = "Blanco";
        coche1.marca = "Audi";
        coche1.modelo = "A7 Avant";
        coche1.cilindrada = 1968;
        System.out.println("El color del coche1 es: " + coche1.color);
        System.out.println("La marca del coche1 es: " + coche1.marca);
        System.out.println("EL modelo del coche1 es: " + coche1.modelo);
        System.out.println("La cilindrada del coche1 es: " + coche1.cilindrada);
        System.out.println();
        System.out.println();
        coche1.arrancar();
        coche1.acelerar();
        coche1.frenar();
            
        }
    }
