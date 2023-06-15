import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;


public class Consumidor{
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        HttpClient htppClient = HttpClient.newHttpClient();


        System.out.println("Digite seu CEP: ");
        int cep = entrada.nextInt();
        

        
        HttpRequest httpRequest = HttpRequest.newBuilder()
        .uri( URI.create("http://127.0.0.1:5000/frete/" + cep))
        .build();

        try{
            HttpResponse<String> httpResponse = htppClient.send(httpRequest, HttpResponse.BodyHandlers.ofString());

            int statusCode = httpResponse.statusCode();
            String responseBody = httpResponse.body();

            
            System.out.println("Status Code:");
            System.out.println(statusCode);
            System.out.println("Response body:");
            System.out.println(responseBody);

        } catch (IOException | InterruptedException e){
            e.printStackTrace();
        }

        entrada.close();
        
    }
}