using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.IO.Compression;





namespace testCompressFiles
{
    class Program
    {
        static void Main(string[] args)
        {

            //data directory
            string path = @"";
            //output directory
            string outfilePath = @"";
            string fileName = "";
            string[] files = Directory.GetFiles(path, "*json");
            int ptr = 0;
            int filecount = 0;
            long filesize = 0;
            filecount = files.Length;


            while (ptr < filecount)
            {
                fileName = Path.GetFileName(files[ptr]);
                fileName += ".zip";
                using (FileStream zipToOpen = new FileStream(outfilePath+ fileName, FileMode.Create))
                {
                    using (ZipArchive archive = new ZipArchive(zipToOpen, ZipArchiveMode.Update))
                    {
                        for (int i = ptr; i < filecount; i++)
                        {
                            string file;
                            file = files[ptr];
                            long length = new System.IO.FileInfo(file).Length;
                            //  * < 95000000
                            filesize += length;

                            if (filesize < 95000000)
                            {
                                archive.CreateEntryFromFile(file, Path.GetFileName(file), CompressionLevel.Optimal);
                                ptr++;
                            }
                            else
                            {
                                Console.WriteLine(fileName);
                                Console.WriteLine(filesize);
                                archive.Dispose();
                                // initial filesize
                                filesize = 0;
                                break;
                            }

                        }



                    }
                }
            }

            
    

        }


    }
}
